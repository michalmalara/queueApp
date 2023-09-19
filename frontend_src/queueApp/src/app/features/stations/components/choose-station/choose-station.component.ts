import {Component, OnInit} from '@angular/core';
import {CommonModule} from '@angular/common';
import {StationService} from "../../services/station.service";
import {MatInputModule} from "@angular/material/input";
import {MatSelectModule} from "@angular/material/select";
import {FormControl, ReactiveFormsModule} from "@angular/forms";
import {Station} from "../../models/station.model";
import {MatButtonModule} from "@angular/material/button";
import {MatCardModule} from "@angular/material/card";
import {Router} from "@angular/router";
import {StationStoreService} from "../../stores/station-store.service";
import {map} from "rxjs/operators";

@Component({
  selector: 'app-choose-station',
  standalone: true,
  imports: [CommonModule, MatInputModule, MatSelectModule, ReactiveFormsModule, MatButtonModule, MatCardModule],
  templateUrl: './choose-station.component.html',
  styleUrls: ['./choose-station.component.scss']
})
export class ChooseStationComponent implements OnInit {
  public stations: Station[] = []

  public stationFormControl = new FormControl<Station | null>(null)

  constructor(
    private stationService: StationService,
    private stationStore: StationStoreService,
    private router: Router
  ) {
  }

  ngOnInit(): void {
    this.stationService.getStations().subscribe((stations) => {
      this.stations = stations
    })
  }

  onSubmit() {
    if (this.stationFormControl.value) {
      this.stationStore.setStation(this.stationFormControl.value)
    }
  }
}
