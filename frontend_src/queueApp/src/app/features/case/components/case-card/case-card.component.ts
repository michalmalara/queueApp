import {Component, Input} from '@angular/core';
import {CommonModule} from '@angular/common';
import {Case} from "../../models/case.model";
import {MatCardModule} from "@angular/material/card";

@Component({
  selector: 'app-case-card',
  standalone: true,
  imports: [CommonModule, MatCardModule],
  templateUrl: './case-card.component.html',
  styleUrls: ['./case-card.component.scss']
})
export class CaseCardComponent {
  @Input() case: Case | undefined;

}
