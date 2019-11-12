package com.example.firebox;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

public class Dashboard extends AppCompatActivity {

    private Button Logout;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);


        Toast.makeText(getApplicationContext(),"Connected",Toast.LENGTH_LONG).show();
        TextView name=findViewById(R.id.name);

        Logout=findViewById(R.id.Logout);
    }
}
