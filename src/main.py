from robots.cleaning_robot import CleaningRobot
from robots.cooking_robot import CookingRobot
from robots.maintenance_robot import MaintenanceRobot
from robots.base_robot import Robot

def main():
    print("Simulation has started..")
    mr_clean = CleaningRobot(name="Mr Clean 1", battery_level=50, status="idle", cleaningtool="vacuum")
    mr_clean.report_status()
    mr_clean.charge()
    mr_clean.clean()
    print(mr_clean.self_diagnose())
    chef_kisses = CookingRobot(name="Chef Kisses 1", battery_level=50, status="idle", cooking_skill="intermediate")

    chef_kisses.report_status()
    chef_kisses.charge()
    chef_kisses.cook()
    print(chef_kisses.self_diagnose())
    multi_tasker = MaintenanceRobot(name="Multi Tasker Pro", battery_level=80, status="idle", cleaningtool="mop", cooking_skill="expert")

    multi_tasker.report_status()
    multi_tasker.charge()
    multi_tasker.clean()
    multi_tasker.cook()
    print(multi_tasker.self_diagnose())

    print("Simulation complete.")

if __name__ == "__main__":
    main()
