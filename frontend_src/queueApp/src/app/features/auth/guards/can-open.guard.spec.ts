import { TestBed } from '@angular/core/testing';

import { CanOpenGuard } from './can-open.guard';

describe('CanOpenGuard', () => {
  let guard: CanOpenGuard;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    guard = TestBed.inject(CanOpenGuard);
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });
});
