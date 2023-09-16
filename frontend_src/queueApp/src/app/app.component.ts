import {Component} from '@angular/core';
import {TopBarComponent} from "./features/structure/top-bar/top-bar.component";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  imports: [
    TopBarComponent
  ],
  standalone: true
})
export class AppComponent {
  title = 'queueApp';
}
