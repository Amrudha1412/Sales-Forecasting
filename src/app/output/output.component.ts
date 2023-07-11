import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-output',
  templateUrl: './output.component.html',
  styleUrls: ['./output.component.css']
})
export class OutputComponent {
  formData={
    QUANTITYORDERED:'',
    PRICEEACH:'',
    MONTH_ID:'',
    YEAR_ID:'',
    DEALSIZE:''
  };
  response:any;
  constructor(private http: HttpClient){}
  onPredict(){
    this.http.post<any[]>('http://127.0.0.1:5000/form',this.formData).subscribe(
      (response) => { this.response = response;},
      (error) => { console.log(error);}
    );
  }
}
