import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(120, 50, 100) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.infer_breach(70, 50, 100) == 'NORMAL')
  
  def test_classify_temperature_breach(self):
    cooling_types=['PASSIVE_COOLING',"HI_ACTIVE_COOLING",'MED_ACTIVE_COOLING']
    upper_limits=[35,45,40]
    for i in range(3):
      self.assertTrue(typewise_alert.classify_temperature_breach(cooling_types[i], -20) == 'TOO_LOW')
      self.assertTrue(typewise_alert.classify_temperature_breach(cooling_types[i], upper_limits[i]+20) == 'TOO_HIGH')
      self.assertTrue(typewise_alert.classify_temperature_breach(cooling_types[i], 20) == 'NORMAL')

  

if __name__ == '__main__':
  unittest.main()
