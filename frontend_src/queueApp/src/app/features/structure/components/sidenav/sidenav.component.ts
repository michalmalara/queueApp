import {Component, OnInit, ViewChild} from '@angular/core';
import {CommonModule} from '@angular/common';
import {RouterOutlet} from "@angular/router";
import {MatSidenav, MatSidenavModule} from "@angular/material/sidenav";
import {SidenavControlService} from "../../services/sidenav-control.service";

@Component({
  selector: 'app-sidenav',
  standalone: true,
  imports: [CommonModule, RouterOutlet, MatSidenavModule],
  templateUrl: './sidenav.component.html',
  styleUrls: ['./sidenav.component.scss']
})
export class SidenavComponent implements OnInit {
  @ViewChild('sidenav') sidenav: MatSidenav | undefined;

  constructor(
    private sidenavControl: SidenavControlService
  ) {
  }

  ngOnInit(): void {
    this.sidenavControl.isSidenavOpen().subscribe((isOpen) => {
      console.log(isOpen)
      if (this.sidenav) {
        if (isOpen) {
          this.sidenav.open()
        } else {
          this.sidenav.close()
        }
      }
    })
  }

}
