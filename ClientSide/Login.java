package com.example.firebox;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.wifi.WifiConfiguration;
import android.net.wifi.WifiManager;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

public class Login extends AppCompatActivity {

    //Initializers
    private Button login;
    private Button Register;
    private EditText Uname;
    private EditText Pass;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        //Variables
        Uname=findViewById(R.id.Uname);
        Pass=findViewById(R.id.Pass);
        login=findViewById(R.id.login);
        Register=findViewById(R.id.Register);



        //Login Button
        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                //Intermediate Variable
                final String Username=Uname.getText().toString();
                final String Password=Pass.getText().toString();

                //python
                if (!Python.isStarted()) {
                    Python.start(new AndroidPlatform(getApplicationContext()));
                }
                Python python = Python.getInstance();
                final PyObject pyObject = python.getModule("priyam");
                PyObject pyObject1 = pyObject.callAttr("hashit", Password);
                String Passfinal = pyObject1.toString();


                Intent connecting = new Intent(getApplicationContext(),connecting.class);
                connecting.putExtra("Uname",Username);
                connecting.putExtra("Pass",Passfinal);
                startActivity(connecting);
                Uname.setText("");
                Pass.setText("");
            }
        });

        //Register Button
        Register.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Uname.setText("");
                Pass.setText("");
                Toast.makeText(getApplicationContext(),"Registered",Toast.LENGTH_LONG).show();
            }
        });

    }
}
