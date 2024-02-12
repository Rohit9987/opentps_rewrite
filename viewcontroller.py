from mainwindow import MainWindow


class Event():
    def __init__(self, *args):
        pass


class ViewController():
    def __init__(self, patientList=0):      # TODO remove =0

        self.crossHairEnabledSignal = Event(bool)
        self.currentPatientChangedSignal = Event(object)
        self.independentViewsEnabledSignal = Event(bool)
        self.profileWidgetEnabledSignal = Event(object)
        self.mainImageChangedSignal = Event(object)
        self.dose1ChangedSignal = Event(object)
        self.dose2ChangedSignal = Event(object)
        self.patientAddedSignal = Event(object)
        self.patientRemovedSignal = Event(object)
        self.secondaryImageChangedSingal = Event(object)
        self.planChangedSignal = Event(object)
        self.showContourSignal = Event(object)
        self.windowLevelEnabledSignal = Event(object)
        self.dropModeSignal = Event(object)
        self.droppedDataSignal = Event(object)
        self.displayLayoutTypeChangedSignal = Event(object)


        self.mainConfig = None

        self._activePatients = []
        self._crossHairEnabled = None
        self._currentPatient = None
        self._dropMode = None # TODO DataViewer.DropModes.DEFAULT
        self._droppedImage = None
        self._independentViewsEnabled = False
        self.profileWidgetCallBack = None           # TODO ProfileWidget.PofileWidgetCallback()
        self._prodileWidgetEnabled = False
        self._mainImage = None
        self._dose1 = None
        self._dose2 = None
        self.multipleActivePatientsEnabled = False      # TODO
        self._patientList = None        # TODO patientList
        self._plan = None
        self._selectedImage = None
        self._windowLevelEnabled = None
        self._displayLayout = None # TODO ViewerPanel.LayoutTypes.DEFAULT
        self.shownDataUIDsList = []  # this is to keep track of which data is currently shown, but not used yet

        self.dynamicDisplayController = None # TODO DynamicDisplayController(self)
        self.mainWindow = MainWindow(self)

        

