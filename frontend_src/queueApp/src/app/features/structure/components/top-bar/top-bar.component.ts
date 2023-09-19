import {Component, OnInit} from '@angular/core';
import {CommonModule} from '@angular/common';
import {MatToolbarModule} from "@angular/material/toolbar";
import {MatIconModule} from "@angular/material/icon";
import {MatButtonModule} from "@angular/material/button";
import {AuthService} from "../../../auth/services/auth.service";
import {SidenavControlService} from "../../services/sidenav-control.service";
import {StationStoreService} from "../../../stations/stores/station-store.service";
import {CustomerStoreService} from "../../../queue/stores/customer-store.service";

@Component({
  selector: 'app-top-bar',
  standalone: true,
  imports: [CommonModule, MatToolbarModule, MatIconModule, MatButtonModule],
  templateUrl: './top-bar.component.html',
  styleUrls: ['./top-bar.component.scss']
})
export class TopBarComponent implements OnInit {
  public assignedStation = ''

  constructor(
    private authService: AuthService,
    private sidenavControl: SidenavControlService,
    private stationStoreService: StationStoreService,
    private customerStoreService: CustomerStoreService
  ) {
  }

  ngOnInit(): void {
  }

  public toggleSidenav() {
    this.sidenavControl.toggleSidenav();
  }

  logout() {
    this.stationStoreService.removeFromStation();
    this.customerStoreService.completeCurrentCustomer();

    this.stationStoreService.state$.subscribe((state) => {
        if (state.station === null) {
          this.authService.logout()
        }
      }
    )
  }
}
