import StepImporter
import CSVExporter
import time


class CoinWatcher:
	"""A Class that regularly pulls data from Bittrex and appends it to a local file"""
	def __init__(self, CoinPairs):
		self.CoinPairs = CoinPairs
		self.ImportMarketData = StepImporter.get_json_from_market #Choose what recorder to use
		self.ExportMarketData = CSVExporter.export_to_file #Choose how to export file

	def step_record(self, CoinPair):
			MarketHistoryJson = self.ImportMarketData(CoinPair)

			self.ExportMarketData(CoinPair, MarketHistoryJson)

	def startwatching(self):
		while 1:
			for CoinPair in self.CoinPairs:
				self.step_record(CoinPair)

			time.sleep(1); #slow process to save electricity 










