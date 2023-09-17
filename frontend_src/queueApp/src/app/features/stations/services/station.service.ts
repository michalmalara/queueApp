import {Injectable} from '@angular/core';
import {RestClientService} from "../../utils/services/rest-client.service";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class StationService {

  constructor(private restClient: RestClientService) {
  }

  getStations(): Observable<any> {
    return this.restClient.get('api/stations/available-stations/')
  }
}
