import {Component, OnInit} from '@angular/core';
import {CommonModule} from '@angular/common';
import {ActivatedRoute} from "@angular/router";
import {QueueService} from "../../features/queue/services/queue.service";
import {CustomerDetails} from "../../features/queue/models/customer-details.model";
import {MatCardModule} from "@angular/material/card";
import {MatListModule} from "@angular/material/list";
import {NgxQRCodeModule} from "@techiediaries/ngx-qrcode";


@Component({
  selector: 'app-queue-details-view',
  standalone: true,
  imports: [CommonModule, MatCardModule, MatListModule, NgxQRCodeModule],
  templateUrl: './queue-details-view.component.html',
  styleUrls: ['./queue-details-view.component.scss'],
})
export class QueueDetailsViewComponent implements OnInit {
  queueData: CustomerDetails | null = null;
  currentUrl: string | null = null;


  constructor(private activatedRoute: ActivatedRoute,
              private queueService: QueueService,
  ) {
  }

  ngOnInit(): void {
    this.currentUrl = window.location.href;


    if (this.activatedRoute.snapshot.params['queueId']) {
      this.queueService.getQueueDetail(this.activatedRoute.snapshot.params['queueId']).subscribe((queueData) => {
        this.queueData = queueData;
      })
    }
  }
}
