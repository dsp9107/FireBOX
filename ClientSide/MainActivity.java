package com.example.firebox;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.net.wifi.WifiConfiguration;
import android.net.wifi.WifiManager;
import android.os.Bundle;
import android.os.Handler;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private static int SPLASH_TIME_OUT = 5000;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //This part Will Enable Wifi
        WifiManager Wifi = (WifiManager) getApplicationContext().getSystemService(Context.WIFI_SERVICE);
        if (Wifi.isWifiEnabled()!=true)
        {
            Wifi.setWifiEnabled(true);
        }

        //Connection to FireBOX's Wifi
        String SSID=getString(R.string.Uname);
        String WifiPass=getString(R.string.Pass);
        WifiConfiguration wifiConfig = new WifiConfiguration();
        wifiConfig.SSID = String.format("\"%s\"",SSID );
        wifiConfig.preSharedKey = String.format("\"%s\"",WifiPass);
        WifiManager wifiManager = (WifiManager) getApplicationContext().getSystemService(WIFI_SERVICE);
        int netId = wifiManager.addNetwork(wifiConfig);
        wifiManager.disconnect();
        wifiManager.enableNetwork(netId, true);
        wifiManager.reconnect();

        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                Intent Login = new Intent(getApplicationContext(),Login.class);
                startActivity(Login);
                finish();
            }
        },SPLASH_TIME_OUT);
    }
}
