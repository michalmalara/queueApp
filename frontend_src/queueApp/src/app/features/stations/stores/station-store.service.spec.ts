import { TestBed } from '@angular/core/testing';

import { StationStoreService } from './station-store.service';

describe('StationStoreService', () => {
  let service: StationStoreService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(StationStoreService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
