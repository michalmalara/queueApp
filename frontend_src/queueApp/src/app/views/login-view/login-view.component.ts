import {Component} from '@angular/core';
import {CommonModule} from '@angular/common';
import {ReactiveFormsModule} from "@angular/forms";
import {LoginFormComponent} from "../../features/auth/components/login-form/login-form.component";
import {MatCardModule} from "@angular/material/card";

@Component({
  selector: 'app-login-view',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, LoginFormComponent, MatCardModule],
  templateUrl: './login-view.component.html',
  styleUrls: ['./login-view.component.scss']
})
export class LoginViewComponent {
  constructor() {
  }
}
