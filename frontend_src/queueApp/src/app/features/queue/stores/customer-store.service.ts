import {Injectable} from '@angular/core';
import {Store} from "../../utils/store/store";
import {CustomerDetails} from "../models/customer-details.model";
import {QueueService} from "../services/queue.service";

export interface CustomerDetailsState {
  customerDetails: CustomerDetails | null;
}

@Injectable({
  providedIn: 'root'
})
export class CustomerStoreService extends Store<CustomerDetailsState> {

  constructor(private queueService: QueueService) {
    super({customerDetails: null});
    this.queueService.getCurrentCustomer().subscribe((customerDetails) => {
      this.setState({
        ...this.getState(),
        customerDetails
      });
    })
  }

  public callNextCustomer() {
    this.queueService.callNextCustomer().subscribe((customerDetails) => {
      this.setState({
        ...this.getState(),
        customerDetails
      });
    })
  }

  public completeCurrentCustomer() {
    this.queueService.completeCurrentCustomer().subscribe((customerDetails) => {
      this.setState({
        ...this.getState(),
        customerDetails
      });
    })
  }
}
