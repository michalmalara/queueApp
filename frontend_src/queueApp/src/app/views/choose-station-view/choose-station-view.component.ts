import {Component} from '@angular/core';
import {CommonModule} from '@angular/common';
import {ChooseStationComponent} from "../../features/stations/components/choose-station/choose-station.component";

@Component({
  selector: 'app-choose-station-view',
  standalone: true,
  imports: [CommonModule, ChooseStationComponent],
  templateUrl: './choose-station-view.component.html',
  styleUrls: ['./choose-station-view.component.scss']
})
export class ChooseStationViewComponent {

}
