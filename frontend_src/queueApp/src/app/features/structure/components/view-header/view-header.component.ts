import {Component, Input} from '@angular/core';
import {CommonModule} from '@angular/common';
import {MatButtonModule} from "@angular/material/button";
import {MatIconModule} from '@angular/material/icon';
import {MatListModule} from "@angular/material/list";
import {Router} from "@angular/router";

@Component({
  selector: 'app-view-header',
  standalone: true,
  imports: [CommonModule, MatButtonModule, MatIconModule, MatListModule],
  templateUrl: './view-header.component.html',
  styleUrls: ['./view-header.component.scss']
})
export class ViewHeaderComponent {
  @Input() title: string | undefined;
  @Input() backUrl: string = '';

  constructor(private router: Router) {
  }

  onBack() {
    this.router.navigate([this.backUrl])
  }
}
