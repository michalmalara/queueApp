import {ComponentFixture, TestBed} from '@angular/core/testing';

import {CallNextCustomerComponent} from './call-next-customer.component';

describe('CallNextCusomerComponent', () => {
  let component: CallNextCustomerComponent;
  let fixture: ComponentFixture<CallNextCustomerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CallNextCustomerComponent]
    })
      .compileComponents();

    fixture = TestBed.createComponent(CallNextCustomerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
