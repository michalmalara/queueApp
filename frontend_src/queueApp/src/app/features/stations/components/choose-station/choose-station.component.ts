import {Component, OnInit} from '@angular/core';
import {CommonModule} from '@angular/common';
import {StationService} from "../../services/station.service";

@Component({
  selector: 'app-choose-station',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './choose-station.component.html',
  styleUrls: ['./choose-station.component.scss']
})
export class ChooseStationComponent implements OnInit {
  public stations = []

  constructor(private stationService: StationService) {
  }

  ngOnInit(): void {
    this.stationService.getStations().subscribe((stations) => {
      this.stations = stations
    })
  }
}
