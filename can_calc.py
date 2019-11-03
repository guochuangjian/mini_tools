class can_calc():
    def __init__(self, clk, max_tseg1, max_tseg2, max_brp):
        self.max_tseg1 = max_tseg1
        self.max_tseg2 = max_tseg2
        self.max_brp   = max_brp
        self.clk       = clk * 1000000

    def calc(self, baudrate, min_sample_point=70, max_sample_point=90):
        bps_table = []
        baudrate *= 1000 
        for brp in range(1, self.max_brp):
            if self.clk / (brp * 4) < baudrate:
                continue
            for tseg1 in range(1, self.max_tseg1):
                for tseg2 in range(1, min(tseg1, self.max_tseg2)):
                    bps = self.clk / (brp * (tseg1 + tseg2 + 1))
                    if bps != baudrate:
                        continue
                    sample_point = (tseg1 + 1) / (tseg1 + tseg2 + 1) * 100
                    if sample_point >= min_sample_point and sample_point <= max_sample_point:
                        bps_value = {}
                        bps_value["brp"]   = brp
                        bps_value["tseg1"] = tseg1 
                        bps_value["tseg2"] = tseg2
                        bps_value["sjw"]   = tseg2
                        bps_value["sample"] = sample_point
                        bps_table.append(bps_value)
        return bps_table

if __name__ == "__main__":
    calc = can_calc(40, 128, 64, 255)
    print(calc.calc(1000))




