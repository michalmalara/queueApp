import { ComponentFixture, TestBed } from '@angular/core/testing';

import { KioskViewComponent } from './kiosk-view.component';

describe('KioskViewComponent', () => {
  let component: KioskViewComponent;
  let fixture: ComponentFixture<KioskViewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ KioskViewComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(KioskViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
