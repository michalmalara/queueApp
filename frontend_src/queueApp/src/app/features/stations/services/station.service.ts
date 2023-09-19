import {Injectable} from '@angular/core';
import {RestClientService} from "../../utils/services/rest-client.service";
import {Observable} from "rxjs";
import {Station, StationRaw} from "../models/station.model";
import {map} from "rxjs/operators";


@Injectable({
  providedIn: 'root'
})
export class StationService {

  constructor(private restClient: RestClientService) {
  }

  getStations(): Observable<Station[]> {
    return this.restClient.get('api/stations/available-stations/').pipe(map((stations: StationRaw[]) => {
          return stations.map((station) => {
              return new Station(station)
            }
          )
        }
      )
    )
  }

  assignUserToStation(station: Station): Observable<null> {
    return this.restClient.post(`api/stations/${station.id}/assign/`, {})
  }

  removeUserFromStation(): Observable<null> {
    return this.restClient.post(`api/stations/remove-user/`, {})
  }

  getCurrentStation(): Observable<Station> {
    return this.restClient.get('api/stations/current/').pipe(map((station: StationRaw) => {
          return new Station(station)
        }
      )
    )
  }
}

