import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChooseStationViewComponent } from './choose-station-view.component';

describe('ChooseStationViewComponent', () => {
  let component: ChooseStationViewComponent;
  let fixture: ComponentFixture<ChooseStationViewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ ChooseStationViewComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ChooseStationViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
