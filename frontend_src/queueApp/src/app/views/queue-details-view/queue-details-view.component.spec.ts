import { ComponentFixture, TestBed } from '@angular/core/testing';

import { QueueDetailsViewComponent } from './queue-details-view.component';

describe('QueueDetailsViewComponent', () => {
  let component: QueueDetailsViewComponent;
  let fixture: ComponentFixture<QueueDetailsViewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ QueueDetailsViewComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(QueueDetailsViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
