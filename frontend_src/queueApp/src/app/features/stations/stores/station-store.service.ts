import {Injectable} from '@angular/core';
import {Store} from "../../utils/store/store";
import {Station} from "../models/station.model";
import {StationService} from "../services/station.service";

export class StationStore {
  station: Station | null

  constructor(station: Station | null) {
    this.station = station
  }
}

const INITIAL_STATE: StationStore = new StationStore(
  null
)


@Injectable({
  providedIn: 'root'
})
export class StationStoreService extends Store<StationStore> {

  constructor(private stationService: StationService) {
    super(INITIAL_STATE)
    this.stationService.getCurrentStation().subscribe((station) => {
      this.setState(
        {
          ...this.getState(),
          station
        }
      )
    })
  }

  public setStation(station: Station) {
    this.stationService.assignUserToStation(station).subscribe(() => {
      this.setState({
        ...this.getState(),
        station
      })
    })
  }

  public removeFromStation() {
    const state = this.getState()
    if (state.station === null) {
      return
    }
    this.stationService.removeUserFromStation().subscribe(() => {
      this.setState({
        ...this.getState(),
        station: null
      })
    })
  }
}
