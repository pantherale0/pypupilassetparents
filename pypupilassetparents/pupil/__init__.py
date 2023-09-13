"""Instance of a single pupil."""

from datetime import datetime
from urllib.parse import quote
from pypupilassetparents.api import PupilAssetAPI
from .timetable import Timetable

class Pupil:
    """Defines a single pupil."""

    def __init__(
        self,
        pupil_parent_id,
        school_id,
        pupil_id,
        parent_id,
        relationship_code,
        online_access,
        physical_access,
        ordering,
        responsibility,
        court_order,
        allow_email,
        allow_text,
        allow_letter,
        preferred,
        first_name,
        surname,
        preferred_first_name,
        preferred_surname,
        middle_name,
        dob,
        gender,
        year_group,
        year_group_offset,
        exit_academic_year,
        email,
        fsm,
        status,
        in_care,
        upn,
        uln,
        candidate_number,
        uci,
        application_reference,
        cloned_from_pupil_id,
        ethnic_code,
        ethnic_sub_group,
        ethnicity_source,
        postcode,
        send,
        sen_other,
        sen_unit,
        resourced_provision,
        late_starter,
        early_leaver,
        young_carer,
        pupil_premium,
        fsm_review_date,
        created_date,
        created_by_user_id,
        mobile,
        mode_of_travel,
        distance_of_travel,
        religion,
        traveller_code,
        enrolment_status,
        guest_school,
        language,
        address_id,
        child_protection,
        services_child,
        gifted,
        app,
        former_upn,
        former_surname,
        part_time,
        hours_at_setting,
        daf_indicator,
        funded_hours,
        extended_hours,
        thirty_hour_code,
        boarder,
        learning_style,
        profile_file_id,
        iep,
        plaa,
        top_up_funding,
        weekly_support_hours,
        groupcall_lock,
        social_worker,
        social_worker_team,
        date_of_entry_to_uk,
        date_of_entry_to_uk_school,
        proof_of_identification,
        date_identification_verified,
        use_target_for_progress,
        notes,
        show_notes_on_profile,
        flexi_schooler,
        eypp,
        eyppbf,
        country_of_birth,
        nationality,
        other_nationality,
        other_mis_number,
        child_in_employment,
        include_in_census,
        in_catchment,
        yssa,
        passport_number,
        saudi_national_id_number,
        visa_type,
        visa_expiry_date,
        min_checkpoint_id,
        legacy_credit,
        meals_credit,
        events_credit,
        misc_credit,
        username,
        key_child,
        critical_worker,
        user_saw_id,
        learner_fam_code,
        learner_fam_hours,
        uifsm,
        shard,
        profile_pic,
        message,
        api
    ):
        """Init a new pupil instance."""
        self.pupil_parent_id: int = int(pupil_parent_id)
        self.school_id: int = int(school_id)
        self.pupil_id: str = str(pupil_id)
        self.parent_id: int = int(parent_id)
        self.relationship_code: str = str(relationship_code)
        self.online_access: int = int(online_access)
        self.physical_access: int = int(physical_access)
        self.ordering: int = int(ordering)
        self.responsibility: int = int(responsibility)
        self.court_order: int = int(court_order)
        self.allow_email: int = int(allow_email)
        self.allow_text: int = int(allow_text)
        self.allow_letter: int = int(allow_letter)
        self.preferred: int = int(preferred)
        self.first_name: str = str(first_name)
        self.surname: str = str(surname)
        self.preferred_first_name: str = str(preferred_first_name)
        self.preferred_surname: str = str(preferred_surname)
        self.middle_name: str = str(middle_name)
        self.dob: str = str(dob)
        self.gender: str = str(gender)
        self.year_group: int = int(year_group)
        self.year_group_offset: int = int(year_group_offset)
        self.exit_academic_year = exit_academic_year
        self.email = email
        self.fsm: int = int(fsm)
        self.status: str = str(status)
        self.in_care: int = int(in_care)
        self.upn: str = str(upn)
        self.uln = uln
        self.candidate_number = candidate_number
        self.uci = uci
        self.application_reference = application_reference
        self.cloned_from_pupil_id = cloned_from_pupil_id
        self.ethnic_code: str = str(ethnic_code)
        self.ethnic_sub_group = ethnic_sub_group
        self.ethnicity_source: str = str(ethnicity_source)
        self.postcode = postcode
        self.send: str = str(send)
        self.sen_other = sen_other
        self.sen_unit: int = int(sen_unit)
        self.resourced_provision: int = int(resourced_provision)
        self.late_starter: int = int(late_starter)
        self.early_leaver: int = int(early_leaver)
        self.young_carer: str = str(young_carer)
        self.pupil_premium: int = int(pupil_premium)
        self.fsm_review_date = fsm_review_date
        self.created_date = created_date
        self.created_by_user_id: int = int(created_by_user_id)
        self.mobile = mobile
        self.mode_of_travel = mode_of_travel
        self.distance_of_travel = distance_of_travel
        self.religion = religion
        self.traveller_code = traveller_code
        self.enrolment_status: str = str(enrolment_status)
        self.guest_school = guest_school
        self.language: str = str(language)
        self.address_id: int = int(address_id)
        self.child_protection: int = int(child_protection)
        self.services_child: int = int(services_child)
        self.gifted: int = int(gifted)
        self.app: int = int(app)
        self.former_upn = former_upn
        self.former_surname = former_surname
        self.part_time: int = int(part_time)
        self.hours_at_setting = hours_at_setting
        self.daf_indicator: int = int(daf_indicator)
        self.funded_hours = funded_hours
        self.extended_hours = extended_hours
        self.thirty_hour_code = thirty_hour_code
        self.boarder: str = str(boarder)
        self.learning_style = learning_style
        self.profile_file_id: int = int(profile_file_id)
        self.iep: int = int(iep)
        self.plaa = plaa
        self.top_up_funding: int = int(top_up_funding)
        self.weekly_support_hours = weekly_support_hours
        self.groupcall_lock: int = int(groupcall_lock)
        self.social_worker = social_worker
        self.social_worker_team = social_worker_team
        self.date_of_entry_to_uk = date_of_entry_to_uk
        self.date_of_entry_to_uk_school = date_of_entry_to_uk_school
        self.proof_of_identification: int = int(proof_of_identification)
        self.date_identification_verified = date_identification_verified
        self.use_target_for_progress: int = int(use_target_for_progress)
        self.notes = notes
        self.show_notes_on_profile: int = int(show_notes_on_profile)
        self.flexi_schooler: int = int(flexi_schooler)
        self.eypp: int = int(eypp)
        self.eyppbf = eyppbf
        self.country_of_birth = country_of_birth
        self.nationality = nationality
        self.other_nationality = other_nationality
        self.other_mis_number = other_mis_number
        self.child_in_employment: int = int(child_in_employment)
        self.include_in_census: int = int(include_in_census)
        self.in_catchment: int = int(in_catchment)
        self.yssa = yssa
        self.passport_number = passport_number
        self.saudi_national_id_number = saudi_national_id_number
        self.visa_type = visa_type
        self.visa_expiry_date = visa_expiry_date
        self.min_checkpoint_id: int = int(min_checkpoint_id)
        self.legacy_credit = legacy_credit
        self.meals_credit = meals_credit
        self.events_credit = events_credit
        self.misc_credit = misc_credit
        self.username = username
        self.key_child: int = int(key_child)
        self.critical_worker: int = int(critical_worker)
        self.user_saw_id = user_saw_id
        self.learner_fam_code = learner_fam_code
        self.learner_fam_hours = learner_fam_hours
        self.uifsm: int = int(uifsm)
        self.shard: str = str(shard)
        self.profile_pic = profile_pic
        self.message = message
        self.timetable: Timetable = None
        self._api: PupilAssetAPI = api

    @classmethod
    def from_dict(cls, data, api) -> 'Pupil':
        """Converts a dict to a pupil."""
        return cls(
            data["pupilParentID"],
            data["schoolID"],
            data["pupilID"],
            data["parentID"],
            data["relationshipCode"],
            data["onlineAccess"],
            data["physicalAccess"],
            data["ordering"],
            data["responsibility"],
            data["courtOrder"],
            data["allowEmail"],
            data["allowText"],
            data["allowLetter"],
            data["preferred"],
            data["firstname"],
            data["surname"],
            data["preferredFirstname"],
            data["preferredSurname"],
            data["middlename"],
            data["dob"],
            data["gender"],
            data["yearGroup"],
            data["yearGroupOffset"],
            data["exitAcademicYear"],
            data["email"],
            data["FSM"],
            data["status"],
            data["inCare"],
            data["UPN"],
            data["ULN"],
            data["candidateNumber"],
            data["UCI"],
            data["applicationReference"],
            data["clonedFromPupilID"],
            data["ethnicCode"],
            data["ethnicSubGroup"],
            data["ethnicitySource"],
            data["postcode"],
            data["SENd"],
            data["SENother"],
            data["senUnit"],
            data["resourcedProvision"],
            data["lateStarter"],
            data["earlyLeaver"],
            data["youngCarer"],
            data["pupilPremium"],
            data["FSMreviewDate"],
            data["createdDate"],
            data["createdByUserID"],
            data["mobile"],
            data["modeOfTravel"],
            data["distanceOfTravel"],
            data["religion"],
            data["travellerCode"],
            data["enrolmentStatus"],
            data["guestSchool"],
            data["language"],
            data["addressID"],
            data["childProtection"],
            data["servicesChild"],
            data["gifted"],
            data["app"],
            data["formerUPN"],
            data["formerSurname"],
            data["partTime"],
            data["hoursAtSetting"],
            data["DAFIndicator"],
            data["fundedHours"],
            data["extendedHours"],
            data["thirtyHourCode"],
            data["boarder"],
            data["learningStyle"],
            data["profileFileID"],
            data["IEP"],
            data["PLAA"],
            data["topUpFunding"],
            data["weeklySupportHours"],
            data["groupcallLock"],
            data["socialWorker"],
            data["socialWorkerTeam"],
            data["dateOfEntryToUK"],
            data["dateOfEntryToUKSchool"],
            data["proofOfIdentification"],
            data["dateIdentificationVerified"],
            data["useTargetForProgress"],
            data["notes"],
            data["showNotesOnProfile"],
            data["flexiSchooler"],
            data["EYPP"],
            data["EYPPBF"],
            data["countryOfBirth"],
            data["nationality"],
            data["otherNationality"],
            data["otherMISNumber"],
            data["childInEmployment"],
            data["includeInCensus"],
            data["inCatchment"],
            data["YSSA"],
            data["passportNumber"],
            data["saudiNationalIDNumber"],
            data["visaType"],
            data["visaExpiryDate"],
            data["minCheckpointID"],
            data["legacyCredit"],
            data["mealsCredit"],
            data["eventsCredit"],
            data["miscCredit"],
            data["username"],
            data["keyChild"],
            data["criticalWorker"],
            data["userSawID"],
            data["learnerFAMcode"],
            data["learnerFAMhours"],
            data["UIFSM"],
            data["shard"],
            data["profilePic"],
            data["message"],
            api
        )

    def update(self, data: dict):
        """Update internal data from a given raw."""
        self.pupil_parent_id = data["pupilParentID"]
        self.school_id = data["schoolID"]
        self.pupil_id = data["pupilID"]
        self.parent_id = data["parentID"]
        self.relationship_code = data["relationshipCode"]
        self.online_access = data["onlineAccess"]
        self.physical_access = data["physicalAccess"]
        self.ordering = data["ordering"]
        self.responsibility = data["responsibility"]
        self.court_order = data["courtOrder"]
        self.allow_email = data["allowEmail"]
        self.allow_text = data["allowText"]
        self.allow_letter = data["allowLetter"]
        self.preferred = data["preferred"]
        self.first_name = data["firstname"]
        self.surname = data["surname"]
        self.preferred_first_name = data["preferredFirstname"]
        self.preferred_surname = data["preferredSurname"]
        self.middle_name = data["middlename"]
        self.dob = data["dob"]
        self.gender = data["gender"]
        self.year_group = data["yearGroup"]
        self.year_group_offset = data["yearGroupOffset"]
        self.exit_academic_year = data["exitAcademicYear"]
        self.email = data["email"]
        self.fsm = data["FSM"]
        self.status = data["status"]
        self.in_care = data["inCare"]
        self.upn = data["UPN"]
        self.uln = data["ULN"]
        self.candidate_number = data["candidateNumber"]
        self.uci = data["UCI"]
        self.application_reference = data["applicationReference"]
        self.cloned_from_pupil_id = data["clonedFromPupilID"]
        self.ethnic_code = data["ethnicCode"]
        self.ethnic_sub_group = data["ethnicSubGroup"]
        self.ethnicity_source = data["ethnicitySource"]
        self.postcode = data["postcode"]
        self.send = data["SENd"]
        self.sen_other = data["SENother"]
        self.sen_unit = data["senUnit"]
        self.resourced_provision = data["resourcedProvision"]
        self.late_starter = data["lateStarter"]
        self.early_leaver = data["earlyLeaver"]
        self.young_carer = data["youngCarer"]
        self.pupil_premium = data["pupilPremium"]
        self.fsm_review_date = data["FSMreviewDate"]
        self.created_date = data["createdDate"]
        self.created_by_user_id = data["createdByUserID"]
        self.mobile = data["mobile"]
        self.mode_of_travel = data["modeOfTravel"]
        self.distance_of_travel = data["distanceOfTravel"]
        self.religion = data["religion"]
        self.traveller_code = data["travellerCode"]
        self.enrolment_status = data["enrolmentStatus"]
        self.guest_school = data["guestSchool"]
        self.language = data["language"]
        self.address_id = data["addressID"]
        self.child_protection = data["childProtection"]
        self.services_child = data["servicesChild"]
        self.gifted = data["gifted"]
        self.app = data["app"]
        self.former_upn = data["formerUPN"]
        self.former_surname = data["formerSurname"]
        self.part_time = data["partTime"]
        self.hours_at_setting = data["hoursAtSetting"]
        self.daf_indicator = data["DAFIndicator"]
        self.funded_hours = data["fundedHours"]
        self.extended_hours = data["extendedHours"]
        self.thirty_hour_code = data["thirtyHourCode"]
        self.boarder = data["boarder"]
        self.learning_style = data["learningStyle"]
        self.profile_file_id = data["profileFileID"]
        self.iep = data["IEP"]
        self.plaa = data["PLAA"]
        self.top_up_funding = data["topUpFunding"]
        self.weekly_support_hours = data["weeklySupportHours"]
        self.groupcall_lock = data["groupcallLock"]
        self.social_worker = data["socialWorker"]
        self.social_worker_team = data["socialWorkerTeam"]
        self.date_of_entry_to_uk = data["dateOfEntryToUK"]
        self.date_of_entry_to_uk_school = data["dateOfEntryToUKSchool"]
        self.proof_of_identification = data["proofOfIdentification"]
        self.date_identification_verified = data["dateIdentificationVerified"]
        self.use_target_for_progress = data["useTargetForProgress"]
        self.notes = data["notes"]
        self.show_notes_on_profile = data["showNotesOnProfile"]
        self.flexi_schooler = data["flexiSchooler"]
        self.eypp = data["EYPP"]
        self.eyppbf = data["EYPPBF"]
        self.country_of_birth = data["countryOfBirth"]
        self.nationality = data["nationality"]
        self.other_nationality = data["otherNationality"]
        self.other_mis_number = data["otherMISNumber"]
        self.child_in_employment = data["childInEmployment"]
        self.include_in_census = data["includeInCensus"]
        self.in_catchment = data["inCatchment"]
        self.yssa = data["YSSA"]
        self.passport_number = data["passportNumber"]
        self.saudi_national_id_number = data["saudiNationalIDNumber"]
        self.visa_type = data["visaType"]
        self.visa_expiry_date = data["visaExpiryDate"]
        self.min_checkpoint_id = data["minCheckpointID"]
        self.legacy_credit = data["legacyCredit"]
        self.meals_credit = data["mealsCredit"]
        self.events_credit = data["eventsCredit"]
        self.misc_credit = data["miscCredit"]
        self.username = data["username"]
        self.key_child = data["keyChild"]
        self.critical_worker = data["criticalWorker"]
        self.user_saw_id = data["userSawID"]
        self.learner_fam_code = data["learnerFAMcode"]
        self.learner_fam_hours = data["learnerFAMhours"]
        self.uifsm = data["UIFSM"]
        self.shard = data["shard"]
        self.profile_pic = data["profilePic"]
        self.message = data["message"]

    async def get_timetable(self, timetable_date: datetime = None):
        """Gets the class timetable for the pupil."""
        if timetable_date is None:
            timetable_date = datetime.now()
        response = await self._api.request_handler(
            endpoint="getTimeCal",
            theDate=timetable_date.strftime("%y-%m-%d"),
            switch="PARENTS",
            pupilRef=str(self.shard)+str(self.pupil_id),
            whatJSON=quote(str({
                "pupilID": self.pupil_id
            }))
        )
        self.timetable = Timetable.from_dict(response["json"])
