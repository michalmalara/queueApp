import {Component} from '@angular/core';
import {CommonModule} from '@angular/common';
import {TopBarComponent} from "../../features/structure/components/top-bar/top-bar.component";
import {RouterOutlet} from "@angular/router";
import {SidenavComponent} from "../../features/structure/components/sidenav/sidenav.component";

@Component({
  selector: 'app-home-view',
  standalone: true,
  imports: [CommonModule, TopBarComponent, RouterOutlet, SidenavComponent],
  templateUrl: './home-view.component.html',
  styleUrls: ['./home-view.component.scss']
})
export class HomeViewComponent {

}
