import {Component} from '@angular/core';
import {CommonModule} from '@angular/common';
import {TopBarComponent} from "../../features/structure/top-bar/top-bar.component";
import {RouterOutlet} from "@angular/router";

@Component({
  selector: 'app-home-view',
  standalone: true,
  imports: [CommonModule, TopBarComponent, RouterOutlet],
  templateUrl: './home-view.component.html',
  styleUrls: ['./home-view.component.scss']
})
export class HomeViewComponent {

}
