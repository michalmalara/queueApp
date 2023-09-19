import {Component, OnInit} from '@angular/core';
import {CommonModule} from '@angular/common';
import {ActivatedRoute, Route} from "@angular/router";

@Component({
  selector: 'app-queue-details-view',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './queue-details-view.component.html',
  styleUrls: ['./queue-details-view.component.scss']
})
export class QueueDetailsViewComponent implements OnInit {
  constructor(private activatedRoute: ActivatedRoute) {
  }

  ngOnInit(): void {
    if (this.activatedRoute.snapshot.params['queueId']) {
      console.log(this.activatedRoute.snapshot.params['queueId']);
    }
  }
}
