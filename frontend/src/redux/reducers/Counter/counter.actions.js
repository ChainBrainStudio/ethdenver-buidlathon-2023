import {  SETDATA, API_CALLED, SUCCESS } from './counter.types';


export const setData = (data) => {

    return {

        type: SETDATA,
        data: data

    };

};

export const itemSuccess = (data) => {
  return {
    type: SUCCESS,
    data: data,
  };
};

export const apiCalled = (data) => {
    return {
      type: API_CALLED,
      data: data
    };
  };