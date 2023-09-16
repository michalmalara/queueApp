import {Component} from '@angular/core';
import {TopBarComponent} from "./features/structure/top-bar/top-bar.component";
import {RouterOutlet} from "@angular/router";
import {MatButtonModule} from "@angular/material/button";
import {RestClientService} from "./features/utils/services/rest-client.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  imports: [
    TopBarComponent,
    RouterOutlet,
    MatButtonModule
  ],
  standalone: true
})
export class AppComponent {
  constructor(private restClient: RestClientService) {
  }

  title = 'queueApp';

}
