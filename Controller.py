class Controller:
    k = 0.0     # Gain
    Ti = 0.0    # Integral Constant
    Tp = 0.0    # Sampling period
    integral_sum = 0.0 # Sum for integral element

    def __init__(self,K,Ti,Tp, IntegralSum) -> None:
        self.k = K
        self.Ti = Ti
        self.Tp = Tp
        self.integral_sum = IntegralSum


    # Parameterization Function
    def parameterize(self, ext_k, ext_Ti, ext_Tp):
        self.k = ext_k
        self.Ti = ext_Ti
        self.Tp = ext_Tp
        self.integral_sum = 0.0
        return 0
    
    # Get Set Point Value function
    def get_sp(self,):
        
        #For future development

        return 0
    
    # Get Actual Value function
    def get_pv(self,):

        #For future development

        return 0 
        
    # Function for calculating actual control value
    def calc_cv(self,sp_value, p_value,):
        upper_limit = 75
        lower_limit = 5
        error_k = sp_value - p_value
        self.integral_sum = self.integral_sum + error_k
        cv = self.k * (error_k + (self.Tp/self.Ti)*(self.integral_sum))
        
        ## limiting the control value and Anti-windup mechanism
        if cv >= upper_limit:
            cv = upper_limit
            self.integral_sum = self.integral_sum - error_k
        if cv <= lower_limit:
            cv = lower_limit
            self.integral_sum = self.integral_sum - error_k

        return cv
