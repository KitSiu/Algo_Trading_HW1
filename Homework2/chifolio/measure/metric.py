# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 14:19:13 2019

@author: Administrator
"""
import pandas as pd
from .measure import ANNUAL_FACTOR, Measure

format_percent = lambda x: str(round(x * 100, 2)) + '%'
format_round_normal = lambda x: round(x, 2)

def create_return_risk_metrics(returns, period='daily'):
    returns = returns.dropna()
    annual_return_ = Measure.cal_cagr(returns, period=period)
    annual_volatility_ = Measure.cal_standard_deviation(returns, period=period)
    sharpe_ratio_ = Measure.cal_sharpe(returns, period=period)
    max_drawdown_ = Measure.cal_max_drawdown(returns)
    omega_ratio_ = Measure.cal_omega(returns)
    calmar_ratio_ = Measure.cal_calmar(returns, period=period)
    sortino_ratio_ = Measure.cal_sortino(returns, period=period)
    res = pd.Series({'annual_return': format_percent(annual_return_), 
                     'annual_volatility': format_percent(annual_volatility_), 
                     'sharpe_ratio': format_round_normal(sharpe_ratio_), 
                     'max_drawdown': format_percent(max_drawdown_), 
                     'omega_ratio': format_round_normal(omega_ratio_), 
                     'calmar_ratio': format_round_normal(calmar_ratio_), 
                     'sortino_ratio': format_round_normal(sortino_ratio_)})
    return res