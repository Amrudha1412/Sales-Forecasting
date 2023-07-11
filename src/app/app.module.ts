import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule} from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { OutputComponent } from './output/output.component';
import { UploadComponent } from './upload/upload.component';
import { ReportComponent } from './report/report.component';
import { FileloadComponent } from './fileload/fileload.component';
import { NgxDropzoneModule } from 'ngx-dropzone';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    OutputComponent,
    UploadComponent,
    ReportComponent,
    FileloadComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    NgxDropzoneModule
    
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }