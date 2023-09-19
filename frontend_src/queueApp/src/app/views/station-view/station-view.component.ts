import {Component, OnInit} from '@angular/core';
import {CommonModule} from '@angular/common';
import {ChooseStationComponent} from "../../features/stations/components/choose-station/choose-station.component";
import {StationStoreService} from "../../features/stations/stores/station-store.service";
import {Station} from "../../features/stations/models/station.model";

import {ViewHeaderComponent} from "../../features/structure/components/view-header/view-header.component";
import {
  CallNextCustomerComponent
} from "../../features/queue/components/call-next-cusomer/call-next-customer.component";
import {CustomerDetails} from "../../features/queue/models/customer-details.model";
import {CustomerStoreService} from "../../features/queue/stores/customer-store.service";
import {CustomerDetailsComponent} from "../../features/queue/components/customer-details/customer-details.component";

@Component({
  selector: 'app-station-view',
  standalone: true,
  imports: [CommonModule, ChooseStationComponent, ViewHeaderComponent, CallNextCustomerComponent, CustomerDetailsComponent],
  templateUrl: './station-view.component.html',
  styleUrls: ['./station-view.component.scss']
})
export class StationViewComponent implements OnInit {
  public station: Station | null = null
  public customerDetails: CustomerDetails | null = null

  constructor(private stationStore: StationStoreService,
              private customerStoreService: CustomerStoreService) {
  }

  ngOnInit(): void {
    this.stationStore.state$.subscribe((state) => {
      this.station = state.station
    })

    this.customerStoreService.state$.subscribe((state) => {
      this.customerDetails = state.customerDetails
    })
  }

}
