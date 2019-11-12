package com.example.firebox;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;

import android.content.Intent;
import android.graphics.Color;
import android.net.Credentials;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.Date;

public class connecting extends AppCompatActivity implements View.OnClickListener {

    public static final int SERVERPORT = 9107;
    private static int SPLASH_TIME_OUT = 3000;
    public static final String SERVER_IP = "192.168.1.10";
    private ClientThread clientThread;
    private Thread thread;

    Bundle Credentials;
    private Handler handler;
    JSONObject Authcheck;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_connecting);

        Credentials = getIntent().getExtras();
        final String Uname = Credentials.getString("Uname");
        String Pass = Credentials.getString("Pass");
        Authcheck = Auth(Uname, Pass);

        handler = new Handler();
        handler.postDelayed(new Runnable() {
            @Override
            public void run() {

                Intent intent=new Intent(getApplicationContext(),Dashboard.class);
                startActivity(intent);
            }
        },SPLASH_TIME_OUT);


    }

    @Override
    public void onClick(View view) {

        if (view.getId() == R.id.connect_server) {
            clientThread = new ClientThread();
            thread = new Thread(clientThread);
            thread.start();

            return; }

             if (view.getId() == R.id.send_data) {
                 String Payloade = String.valueOf(Pack(Authcheck));
                 int HEADERSIZE = 10;
                 byte b[] = null;
                 String Authentication = padLeft(String.valueOf(Payloade.length()), HEADERSIZE) + Payloade;

                 try {
                     b=Authentication.getBytes("Utf8");

                 }catch (UnsupportedEncodingException e)
                 {
                     e.printStackTrace();
                 }
                 if (clientThread!=null) {
                     Toast.makeText(getApplicationContext(),"Connecting",Toast.LENGTH_LONG).show();

                     clientThread.sendMessage(b);

                 }



        }

    }

    class ClientThread implements Runnable {

        private Socket socket;
        private BufferedReader input;

        @Override
        public void run() {

            try {
                InetAddress serverAddr = InetAddress.getByName(SERVER_IP);
                socket = new Socket(serverAddr, SERVERPORT);

                while (!Thread.currentThread().isInterrupted()) {

                    this.input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                    String message = input.readLine();
                    if (null == message || "Disconnect".contentEquals(message)) {
                        Thread.interrupted();
                        break;
                    }
                }

            } catch (UnknownHostException e1) {
                e1.printStackTrace();
            } catch (IOException e1) {
                e1.printStackTrace();
            }

        }

        void sendMessage(final byte []message) {
            new Thread(new Runnable() {
                @Override
                public void run() {
                    try {
                        if (null != socket) {
                            DataOutputStream dataOutputStream=new DataOutputStream(socket.getOutputStream());
                            dataOutputStream.write(message);

                        }
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }
            }).start();

        }

    }


    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (null != clientThread) {
            byte []nz=null;
            clientThread.sendMessage(nz);
            clientThread = null;
        }
    }

    public JSONObject Pack(JSONObject m) {
        JSONObject jsonObject = new JSONObject();
        try {
            jsonObject.put("messageType", "login");
            jsonObject.put("messageLength", m.length());
            jsonObject.put("messageContent", m);
        }
        catch (JSONException z) {
            System.out.print("");
        }
        return jsonObject;
    }

    public JSONObject Auth(String uname,String pass)
    {
        JSONObject jsonObject=new JSONObject();
        try {
            jsonObject.put("uname",uname);
            jsonObject.put("pwd",pass);

        }catch (JSONException z)
        {z.printStackTrace();}
        return jsonObject;
    }

    public static String padLeft(String s, int n) {
        return String.format("%" + n + "s", s);
    }


}
