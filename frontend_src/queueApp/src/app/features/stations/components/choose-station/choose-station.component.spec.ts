import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChooseStationComponent } from './choose-station.component';

describe('ChooseStationComponent', () => {
  let component: ChooseStationComponent;
  let fixture: ComponentFixture<ChooseStationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ ChooseStationComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ChooseStationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
