import {Injectable} from '@angular/core';
import {RestClientService} from "../../utils/services/rest-client.service";
import {Observable, throwError} from "rxjs";
import {CustomerDetails, CustomerDetailsModelRaw} from "../models/customer-details.model";
import {catchError, map} from "rxjs/operators";
import {MatSnackBar} from "@angular/material/snack-bar";

@Injectable({
  providedIn: 'root'
})
export class QueueService {

  constructor(private restClient: RestClientService,
              private snackBar: MatSnackBar) {
  }

  public createQueue(caseId: number) {
    return this.restClient.post('api/queue/', {case: caseId}).pipe(
      map((response) => {
          return new CustomerDetails(response)
        }
      ))
  }

  public callNextCustomer(): Observable<CustomerDetails> {
    return this.restClient.post('api/queue/call-next/', {}).pipe(
      map((response) => {
          return new CustomerDetails(response)
        }
      ),
      catchError((error) => {
          if (error.status === 400) {
            this.snackBar.open('There are no clients in the queue', 'Close', {
              duration: 5000,
            });
          }
          return throwError(error);
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

  public getQueueDetail(queueId: number): Observable<CustomerDetails> {
    return this.restClient.get(`api/queue/${queueId}/details/`).pipe(
      map((response) => new CustomerDetails(response)))
  }
}
