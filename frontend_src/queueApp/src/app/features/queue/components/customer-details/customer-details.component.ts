import {Component, OnInit} from '@angular/core';
import {CommonModule} from '@angular/common';
import {CustomerStoreService} from "../../stores/customer-store.service";
import {CustomerDetails} from "../../models/customer-details.model";
import {MatCardModule} from "@angular/material/card";
import {MatListModule} from "@angular/material/list";

@Component({
  selector: 'app-customer-details',
  standalone: true,
  imports: [CommonModule, MatCardModule, MatListModule],
  templateUrl: './customer-details.component.html',
  styleUrls: ['./customer-details.component.scss']
})
export class CustomerDetailsComponent implements OnInit {
  public customerDetails: CustomerDetails | null = null

  constructor(private customerStoreService: CustomerStoreService) {
  }

  ngOnInit(): void {
    this.customerStoreService.state$.subscribe((state) => {
      this.customerDetails = state.customerDetails
    })
  }

}
