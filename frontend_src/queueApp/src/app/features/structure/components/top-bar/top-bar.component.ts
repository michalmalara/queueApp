import {Component, OnInit} from '@angular/core';
import {CommonModule} from '@angular/common';
import {MatToolbarModule} from "@angular/material/toolbar";
import {MatIconModule} from "@angular/material/icon";
import {MatButtonModule} from "@angular/material/button";
import {AuthService} from "../../../auth/services/auth.service";
import {SidenavControlService} from "../../services/sidenav-control.service";

@Component({
  selector: 'app-top-bar',
  standalone: true,
  imports: [CommonModule, MatToolbarModule, MatIconModule, MatButtonModule],
  templateUrl: './top-bar.component.html',
  styleUrls: ['./top-bar.component.scss']
})
export class TopBarComponent implements OnInit {

  constructor(
    private authService: AuthService,
    private sidenavControl: SidenavControlService
  ) {
  }

  ngOnInit(): void {
  }

  public toggleSidenav() {
    this.sidenavControl.toggleSidenav();
  }

  logout() {
    this.authService.logout()
  }
}
