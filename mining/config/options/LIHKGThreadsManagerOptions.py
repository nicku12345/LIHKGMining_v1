"""
Defines the options for LIHKGThreadsManager
"""
from typing import List
from dataclasses import dataclass, field


@dataclass
class LIHKGCategoryOption:
    """
    Options for specifying what categories to fetch
    """
    CategoryId      : int
    ToFetch         : bool

@dataclass
class LIHKGThreadsManagerOptions:
    """
    Options for LIHKGThreadsManager.
    """

    # Used for fetching threads. Introduces a sleep between page fetches with
    # duration randomly chosen in the open interval (0, _sleep_time).
    # Its purpose is to create a more dynamic and less machinery behavior.
    # Default is 3 seconds
    SleepTime               : int = 3

    # Used for fetching threads. The fetch will retry on failure,
    # and stop once reaching this threshold
    # Default is 3 times
    MaxFailureCount         : int = 3

    # Used for determining which categories are to be fetched.
    LIHKGCategoryOptions    : List[LIHKGCategoryOption] = field(default_factory=lambda: [
        LIHKGCategoryOption(CategoryId=1, ToFetch=True),	# 吹水台
        LIHKGCategoryOption(CategoryId=999, ToFetch=False),	# 自選台
        LIHKGCategoryOption(CategoryId=2, ToFetch=True),	# 熱　門
        LIHKGCategoryOption(CategoryId=3, ToFetch=True),	# 最　新
        LIHKGCategoryOption(CategoryId=4, ToFetch=True),	# 手機台
        LIHKGCategoryOption(CategoryId=5, ToFetch=True),	# 時事台
        LIHKGCategoryOption(CategoryId=33, ToFetch=True),	# 政事台
        LIHKGCategoryOption(CategoryId=38, ToFetch=True),	# World
        LIHKGCategoryOption(CategoryId=6, ToFetch=True),	# 體育台
        LIHKGCategoryOption(CategoryId=7, ToFetch=True),	# 娛樂台
        LIHKGCategoryOption(CategoryId=8, ToFetch=True),	# 動漫台
        LIHKGCategoryOption(CategoryId=9, ToFetch=True),	# Apps台
        LIHKGCategoryOption(CategoryId=10, ToFetch=True),	# 遊戲台
        LIHKGCategoryOption(CategoryId=11, ToFetch=True),	# 影視台
        LIHKGCategoryOption(CategoryId=12, ToFetch=True),	# 講故台
        LIHKGCategoryOption(CategoryId=36, ToFetch=True),	# 健康台
        LIHKGCategoryOption(CategoryId=30, ToFetch=True),	# 感情台
        LIHKGCategoryOption(CategoryId=13, ToFetch=True),	# 潮流台
        LIHKGCategoryOption(CategoryId=14, ToFetch=True),	# 上班台
        LIHKGCategoryOption(CategoryId=15, ToFetch=True),	# 財經台
        LIHKGCategoryOption(CategoryId=37, ToFetch=True),	# 房屋台
        LIHKGCategoryOption(CategoryId=16, ToFetch=True),	# 飲食台
        LIHKGCategoryOption(CategoryId=17, ToFetch=True),	# 旅遊台
        LIHKGCategoryOption(CategoryId=18, ToFetch=True),	# 學術台
        LIHKGCategoryOption(CategoryId=19, ToFetch=True),	# 校園台
        LIHKGCategoryOption(CategoryId=20, ToFetch=True),	# 汽車台
        LIHKGCategoryOption(CategoryId=21, ToFetch=True),	# 音樂台
        LIHKGCategoryOption(CategoryId=31, ToFetch=True),	# 創意台
        LIHKGCategoryOption(CategoryId=22, ToFetch=True),	# 硬件台
        LIHKGCategoryOption(CategoryId=23, ToFetch=True),	# 攝影台
        LIHKGCategoryOption(CategoryId=24, ToFetch=True),	# 玩具台
        LIHKGCategoryOption(CategoryId=25, ToFetch=True),	# 寵物台
        LIHKGCategoryOption(CategoryId=26, ToFetch=True),	# 軟件台
        LIHKGCategoryOption(CategoryId=27, ToFetch=True),	# 活動台
        LIHKGCategoryOption(CategoryId=35, ToFetch=True),	# 電訊台
        LIHKGCategoryOption(CategoryId=34, ToFetch=True),	# 直播台
        LIHKGCategoryOption(CategoryId=28, ToFetch=True),	# 站務台
        LIHKGCategoryOption(CategoryId=29, ToFetch=False),	# 成人台
        LIHKGCategoryOption(CategoryId=32, ToFetch=True)	# 黑　洞
    ])

    def ApplyOptions(self, LIHKGThreadsManagerCls):
        """
        Apply the options to the LIHKGThreadsManager class.

        :param LIHKGThreadsManagerCls: The class of LIHKGThreadsManager
        """
        LIHKGThreadsManagerCls._options = self
