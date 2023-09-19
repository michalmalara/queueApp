import {Component} from '@angular/core';
import {CommonModule} from '@angular/common';
import {QueueService} from "../../features/queue/services/queue.service";
import {CaseService} from "../../features/case/services/case.service";
import {Case} from "../../features/case/models/case.model";
import {CaseCardComponent} from "../../features/case/components/case-card/case-card.component";
import {Router} from "@angular/router";

@Component({
  selector: 'app-kiosk-view',
  standalone: true,
  imports: [CommonModule, CaseCardComponent],
  templateUrl: './kiosk-view.component.html',
  styleUrls: ['./kiosk-view.component.scss']
})
export class KioskViewComponent {

  public cases: Case[] = []

  constructor(private queueService: QueueService, private caseService: CaseService, private router: Router) {
  }

  ngOnInit(): void {
    this.caseService.getCases().subscribe((cases: Case[]) => {
      this.cases = cases;
    })
  }


  onCaseClicked(_case: Case) {
    this.queueService.createQueue(_case.id).subscribe((queue) => {
      this.router.navigate(['queue', queue.id])
    })
  }
}
