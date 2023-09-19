import {Injectable} from '@angular/core';
import {RestClientService} from "../../utils/services/rest-client.service";
import {map} from "rxjs/operators";
import {Observable} from "rxjs";
import {Case} from "../models/case.model";

@Injectable({
  providedIn: 'root'
})
export class CaseService {

  constructor(private restClient: RestClientService) {
  }

  getCases(): Observable<Case[]> {
    return this.restClient.get('api/case/').pipe(
      map((response) => {
          return response.map((item: any) => new Case(item))
        }
      )
    )
  }
}
