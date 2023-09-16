import {Component} from '@angular/core';
import {TopBarComponent} from "./features/structure/top-bar/top-bar.component";
import {RouterOutlet} from "@angular/router";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  imports: [
    TopBarComponent,
    RouterOutlet
  ],
  standalone: true
})
export class AppComponent {
  title = 'queueApp';
}
