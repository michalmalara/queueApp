import {Injectable} from '@angular/core';
import {RestClientService} from "../../utils/services/rest-client.service";
import {Observable} from "rxjs";
import {CustomerDetails} from "../models/customer-details.model";
import {map} from "rxjs/operators";

@Injectable({
  providedIn: 'root'
})
export class QueueService {

  constructor(private restClient: RestClientService) {
  }

  public callNextCustomer(): Observable<CustomerDetails> {
    return this.restClient.post('api/queue/call-next/', {}).pipe(
      map((response) => {
          return new CustomerDetails(response)
        }
      ))
  }

  public getCurrentCustomer(): Observable<CustomerDetails> {
    return this.restClient.get('api/queue/current/').pipe(
      map((response) => {
          return new CustomerDetails(response)
        }
      ))
  }

  public completeCurrentCustomer(): Observable<CustomerDetails> {
    return this.restClient.post('api/queue/complete/', {}).pipe(
      map((response) => {
          return new CustomerDetails(response)
        }
      ))
  }
}
