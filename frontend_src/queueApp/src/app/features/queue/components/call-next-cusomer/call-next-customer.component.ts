import {Component, OnInit} from '@angular/core';
import {CommonModule} from '@angular/common';
import {MatButtonModule} from "@angular/material/button";
import {CustomerStoreService} from "../../stores/customer-store.service";
import {CustomerDetails} from "../../models/customer-details.model";

@Component({
  selector: 'app-call-next-customer',
  standalone: true,
  imports: [CommonModule, MatButtonModule],
  templateUrl: './call-next-customer.component.html',
  styleUrls: ['./call-next-customer.component.scss']
})
export class CallNextCustomerComponent implements OnInit {
  public customerDetails: CustomerDetails | null = null;

  constructor(private customerStoreService: CustomerStoreService) {
  }

  ngOnInit(): void {
    this.customerStoreService.state$.subscribe((state) => {
      this.customerDetails = state.customerDetails
    })
  }

  onCallNextCustomer() {
    this.customerStoreService.callNextCustomer();
  }

  onCompleteCase() {
    this.customerStoreService.completeCurrentCustomer();
  }
}
