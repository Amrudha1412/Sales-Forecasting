import { NgModule } from '@angular/core';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { OutputComponent } from './output/output.component';
import { UploadComponent } from './upload/upload.component';
import { ReportComponent } from './report/report.component';
import { FileloadComponent } from './fileload/fileload.component';


const routes: Routes = [{
  path:'',component:LoginComponent
},{
  path:'login', component:FileloadComponent
},{
  path:'predict',component:OutputComponent

},{
  path:'report',component:ReportComponent
}];

@NgModule({
  imports: [RouterModule.forRoot(routes) , ReactiveFormsModule, FormsModule],
  exports: [RouterModule]
})
export class AppRoutingModule { }
