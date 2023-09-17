import {Component} from '@angular/core';
import {CommonModule} from '@angular/common';
import {FormBuilder, FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators} from "@angular/forms";
import {Router} from "@angular/router";
import {AuthService} from "../../services/auth.service";
import {MatInputModule} from "@angular/material/input";
import {MatButtonModule} from "@angular/material/button";

@Component({
  selector: 'app-login-form',
  standalone: true,
  imports: [CommonModule, FormsModule, ReactiveFormsModule, MatInputModule, MatButtonModule],
  templateUrl: './login-form.component.html',
  styleUrls: ['./login-form.component.scss']
})
export class LoginFormComponent {
  public form: FormGroup;
  public usernameFieldControl = new FormControl('', Validators.required);
  public passwordFieldControl = new FormControl('', Validators.required);

  public loginFailed = false;

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private router: Router
  ) {

    this.form = this.fb.group({
      username: this.usernameFieldControl,
      password: this.passwordFieldControl
    });
  }

  login() {
    const val = this.form.value;


    if (this.usernameFieldControl.value && this.passwordFieldControl.value) {
      this.authService.login(val.username, val.password).subscribe(() => {
          this.router.navigate(['/choose-station'])
        },
        (err) => this.loginFailed = true
      );
    }
  }
}

