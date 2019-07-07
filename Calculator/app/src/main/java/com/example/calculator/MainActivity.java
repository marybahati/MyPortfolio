package com.example.calculator;

import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
TextView Result;
EditText ed1,ed2;
Button add,subtract,multiply,divide;
float result_num;
int num1,num2;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);


        Result = (TextView)findViewById(R.id.Results);
        ed1=(EditText)findViewById(R.id.ed1);
        ed2=(EditText)findViewById(R.id.ed2);
        add =(Button)findViewById(R.id.add);
        subtract =(Button)findViewById(R.id.subtract);
        multiply =(Button)findViewById(R.id.multiply);
        divide =(Button)findViewById(R.id.divide);

        add.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                num1=Integer.parseInt(ed1.getText().toString());
                num2=Integer.parseInt(ed2.getText().toString());
                result_num=num1 + num2;
                Result.setText(String.valueOf(result_num));
            }
        });

        subtract.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                num1=Integer.parseInt(ed1.getText().toString());
                num2=Integer.parseInt(ed2.getText().toString());
                result_num=num1 - num2;
                Result.setText(String.valueOf(result_num));
            }
        });


        multiply.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                num1=Integer.parseInt(ed1.getText().toString());
                num2=Integer.parseInt(ed2.getText().toString());
                result_num=num1*num2;
                Result.setText(String.valueOf(result_num));
            }
        });

        divide.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                num1=Integer.parseInt(ed1.getText().toString());
                num2=Integer.parseInt(ed2.getText().toString());
                result_num=num1/num2;
                Result.setText(String.valueOf(result_num));
            }
        });


    }
}
