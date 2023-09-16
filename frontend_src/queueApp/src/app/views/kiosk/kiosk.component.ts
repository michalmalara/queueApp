import {Component, OnInit} from '@angular/core';
import {CommonModule} from '@angular/common';

@Component({
  selector: 'app-kiosk',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './kiosk.component.html',
  styleUrls: ['./kiosk.component.scss']
})
export class KioskComponent implements OnInit {
  constructor() {
    console.log('KioskComponent')
  }

  ngOnInit(): void {
  }

}
