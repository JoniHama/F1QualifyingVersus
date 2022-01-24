import logging
import pandas as pd
import csv


# to do:
# colors palette for the constructors
# year by year basis - change the window then
# year by year average on the side

def create_column(season, races, qualitimestable, qualidifference, endoftheseasondata, drivername, missedraces,
                  qualitimes_ignored):
    season = season-1
    print("End of the season data for ", drivername, " ", endoftheseasondata)
    print("Qualitimestable ", qualitimestable)
    print("Qualidifference ", qualidifference)
    print("Qualitimes_ignored ", qualitimes_ignored)

    #if season == 2005:
        #for x in range(1, 7):
            #qualitimestable[x]["driver"] = twothousandfive_quali[x]

       # qualitimestable["driver"] = twothousandfive_quali[1]


    columndata = {1: {}}
    columndata2 = {}
    columndata3 = {}
    print(qualitimestable[1]['driver'])
    for x in range(1, races):
        print("X ", x)
        #if x >= 17:
            #print("x >= 17")

        if x != 1 and columndata2:
            try:
                if qualidifference[x - 1]['teammate'] != qualidifference[x]['teammate']:
                    if endoftheseasondata[0]['teammate'] == qualidifference[x]['teammate']:
                        if season == 2005 and x < 7:
                            columndata[x] = {drivername.capitalize(): "aggregate",
                                             qualidifference[x]['teammate'].capitalize(): "aggregate", "Gap": qualidifference[x]['time']
                                             }
                        else:
                            columndata[x] = {drivername.capitalize(): qualitimestable[x]['driver'],
                                              qualidifference[x]['teammate'].capitalize(): qualitimestable[x]['teammate'],
                                              "Gap": qualidifference[x]['time']
                                              }
                    else:
                        columndata3[x] = {drivername.capitalize(): qualitimestable[x]['driver'],
                                          qualidifference[x]['teammate'].capitalize(): qualitimestable[x]['teammate'],
                                          "Gap": qualidifference[x]['time']
                                          }
                        if season == 2005 and x < 7:
                            pass
                        else:
                            columndata2[x - 1] = {drivername.capitalize(): qualitimestable[x - 1]['driver'],
                                                  qualidifference[x - 1]['teammate'].capitalize(): qualitimestable[x - 1][
                                                      'teammate'],
                                                  "Gap": qualidifference[x - 1]['time'],
                                                  "Average gap": endoftheseasondata[1]['time']
                                                  }
            except Exception as ex:
                print(ex)
        try:
            if not columndata2 or endoftheseasondata[0].get("teammate") == qualidifference[x].get("teammate"): # Oh! I didn't know .get was a thing for dictionaries. Would have saved a lot of trouble with try: expect statements. Oh well.
                try:
                    if season == 2005 and x < 7:
                        if endoftheseasondata[0]['teammate'] == qualidifference[x]['teammate']:
                            columndata[x] = {drivername.capitalize(): "aggregate",
                                             qualidifference[x]['teammate'].capitalize(): "aggregate",
                                             "Gap": qualidifference[x]['time']
                                             }
                        else:
                            columndata2[x] = {drivername.capitalize(): "aggregate",
                                              qualidifference[x]['teammate'].capitalize(): "aggregate",
                                              "Gap": qualidifference[x]['time']
                                              }
                    else:
                        if not qualitimestable[x]['driver']:
                            columndata[x] = {drivername.capitalize(): qualitimes_ignored[x]['driver'],
                                             qualitimes_ignored[x]['teammatename'].capitalize(): qualitimes_ignored[x][
                                                 'teammate'],
                                             "Gap": "---"
                                             }
                        else:
                            if endoftheseasondata[0]['teammate'] == qualidifference[x]['teammate']:
                                columndata[x] = {drivername.capitalize(): qualitimestable[x]['driver'],
                                                 qualidifference[x]['teammate'].capitalize(): qualitimestable[x]['teammate'],
                                                 "Gap": qualidifference[x]['time']
                                                 }
                            else:
                                columndata2[x] = {drivername.capitalize(): qualitimestable[x]['driver'],
                                                  qualidifference[x]['teammate'].capitalize(): qualitimestable[x][
                                                      'teammate'],
                                                  "Gap": qualidifference[x]['time']
                                                  }
                                columndata[x - 1] = {drivername.capitalize(): qualitimestable[x - 1]['driver'],
                                                      qualidifference[x - 1]['teammate'].capitalize():
                                                          qualitimestable[x - 1][
                                                              'teammate'],
                                                      "Gap": qualidifference[x - 1]['time'],
                                                      "Average gap": endoftheseasondata[0]['time']
                                                      }

                except Exception as ex:  # to-do, include driver times even without gap data
                    # columndata[x] = {"---": "---",
                    #             "---": "---",
                    #             "Gap": "---"
                    #            }
                    if season == 2005 and x < 7:
                        columndata[x] = {drivername.capitalize(): qualitimestable[x]['driver'],
                                         qualidifference[x]['teammate'].capitalize(): "aggregate",
                                         "Gap": qualidifference[x]['time']
                                         }
                    else:
                        if endoftheseasondata[0]['teammate'] == qualitimes_ignored[x]['teammatename']:
                            columndata[x] = {drivername.capitalize(): qualitimes_ignored[x]['driver'],
                                             qualitimes_ignored[x]['teammatename'].capitalize(): qualitimes_ignored[x]['teammate'],
                                             "Gap": "---"
                                             }
                        else:
                            pass
                    print("Exception! ", ex)
            elif not columndata3:
                try:
                    if season == 2005 and x < 7:
                        columndata2[x] = {drivername.capitalize(): "aggregate",
                                         qualidifference[x]['teammate'].capitalize(): "aggregate",
                                         "Gap": qualidifference[x]['time']
                                         }
                    else:
                        try:
                            columndata[x]
                        except Exception:
                            try:
                                columndata[x]
                            except Exception:
                                columndata2[x] = {drivername.capitalize(): qualitimestable[x]['driver'],
                                              qualidifference[x]['teammate'].capitalize(): qualitimestable[x]['teammate'],
                                              "Gap": qualidifference[x]['time']
                                              }
                except Exception as ex:
                    print("Exception! ", ex)
            else:
                try:
                    if season == 2005 and x < 7:
                        if endoftheseasondata[0]['teammate'] == qualidifference[x]['teammate']:
                            columndata[x] = {drivername.capitalize(): "aggregate",
                                             qualidifference[x]['teammate'].capitalize(): "aggregate",
                                             "Gap": qualidifference[x]['time']
                                             }
                        else:
                            columndata3[x] = {drivername.capitalize(): "aggregate",
                                              qualidifference[x]['teammate'].capitalize(): "aggregate",
                                              "Gap": qualidifference[x]['time']
                                              }
                    else:
                        if endoftheseasondata[0]['teammate'] == qualidifference[x]['teammate']:
                            columndata[x] = {drivername.capitalize(): qualitimestable[x]['driver'],
                                              qualidifference[x]['teammate'].capitalize(): qualitimestable[x]['teammate'],
                                              "Gap": qualidifference[x]['time']
                                              }
                        else:
                            try:
                                columndata3[x] = {drivername.capitalize(): qualitimestable[x]['driver'],
                                                  qualidifference[x]['teammate'].capitalize(): qualitimestable[x]['teammate'],
                                                  "Gap": qualidifference[x]['time']
                                                  }
                            except Exception:
                                columndata3[x] = {drivername.capitalize(): qualitimes_ignored[x]['driver'],
                                                  qualitimes_ignored[x]['teammatename'].capitalize(): qualitimes_ignored[x]['teammate'],
                                                  "Gap": "---"
                                                  }
                except Exception:
                    try:
                        if endoftheseasondata[0]['teammate'] == qualidifference[x]['teammate']:
                            columndata[x] = {drivername.capitalize(): qualitimestable[x]['driver'],
                                             qualidifference[x]['teammate'].capitalize(): qualitimestable[x]['teammate'],
                                             "Gap": qualidifference[x]['time']
                                             }
                        else:
                            columndata3[x] = {drivername.capitalize(): qualitimes_ignored[x]['driver'],
                                              qualitimes_ignored[x]['teammatename'].capitalize(): qualitimes_ignored[x]['teammate'],
                                              "Gap": "---"
                                              }
                    except Exception:
                        if endoftheseasondata[0]['teammate'] == qualitimes_ignored[x]['teammatename']:
                            columndata[x] = {drivername.capitalize(): qualitimes_ignored[x]['driver'],
                                             qualitimes_ignored[x]['teammatename'].capitalize(): qualitimes_ignored[x]['teammate'],
                                             "Gap": "---"
                                             }
                        else:
                            columndata3[x] = {drivername.capitalize(): qualitimes_ignored[x]['driver'],
                                              qualitimes_ignored[x]['teammatename'].capitalize(): qualitimes_ignored[x]['teammate'],
                                              "Gap": "---"
                                              }
        except Exception:
            if season == 2005 and x < 7:
                columndata[x] = {drivername.capitalize(): "aggregate",
                                 qualitimes_ignored[x]['teammatename'].capitalize(): "aggregate",
                                 "Gap": "---"
                                 }
            else:
                if columndata3 and endoftheseasondata[0]['teammate'] != qualitimes_ignored[x]['teammatename']:
                    columndata3[x] = {drivername.capitalize(): qualitimes_ignored[x]['driver'],
                                     qualitimes_ignored[x]['teammatename'].capitalize(): qualitimes_ignored[x]['teammate'],
                                     "Gap": "---"
                                     }
                elif columndata2 and endoftheseasondata[0]['teammate'] != qualitimes_ignored[x]['teammatename']:
                    columndata2[x] = {drivername.capitalize(): qualitimes_ignored[x]['driver'],
                                     qualitimes_ignored[x]['teammatename'].capitalize(): qualitimes_ignored[x]['teammate'],
                                     "Gap": "---"
                                     }
                else:
                    columndata[x] = {drivername.capitalize(): qualitimes_ignored[x]['driver'],
                                     qualitimes_ignored[x]['teammatename'].capitalize(): qualitimes_ignored[x]['teammate'],
                                     "Gap": "---"
                                     }


        if not columndata3:
            try:
                if x != 1 and qualidifference[x - missedraces - 1]['teammate'] != qualidifference[x - missedraces][
                    'teammate']:  # if multiple drivers

                    if season == 2005 and x < 7:
                        columndata2[x] = {drivername.capitalize(): "aggregate",
                                          qualidifference[x]['teammate'].capitalize(): "aggregate",
                                          "Gap": qualidifference[x]['time']
                                          }
                    else:
                        try:
                            columndata[x]
                        except Exception:
                            columndata2[x] = {drivername.capitalize(): qualitimestable[x]['driver'],
                                          qualidifference[x]['teammate'].capitalize(): qualitimestable[x]['teammate'],
                                          "Gap": qualidifference[x]['time']
                                          }
                        '''columndata[x - 1] = {drivername.capitalize(): qualitimestable[x - 1]['driver'],
                                             qualidifference[x - 1]['teammate'].capitalize(): qualitimestable[x - 1][
                                                 'teammate'],
                                             "Gap": qualidifference[x - 1]['time'],
                                             "Average gap": endoftheseasondata[0]['time']
                                             }'''
            except Exception as ex:
                try:
                    if columndata2:
                        columndata2[x] = {drivername.capitalize(): qualitimes_ignored[x]['driver'],
                                          qualitimes_ignored[x]['teammatename'].capitalize(): qualitimes_ignored[x][
                                              'teammate'],
                                          "Gap": "ignored"
                                          }
                except Exception as ex:
                    print(ex)

        if x == races-1:
            try:
                if not columndata3 and columndata2 and endoftheseasondata[0]['teammate'] != qualidifference[x]['teammate']:
                    try:
                        columndata2[x] = {drivername.capitalize(): qualitimestable[x]['driver'],
                                          qualidifference[x]['teammate'].capitalize(): qualitimestable[x]['teammate'],
                                          "Gap": qualidifference[x]['time']
                                          }
                        columndata2[x + 1] = {drivername.capitalize(): qualitimestable[x + 1]['driver'],
                                              qualidifference[x + 1]['teammate'].capitalize(): qualitimestable[x + 1][
                                                  'teammate'],
                                              "Gap": qualidifference[x + 1]['time'],
                                              "Average gap": endoftheseasondata[1]['time']
                                              }
                    except Exception as ex:
                        print(ex)
            except Exception:
                columndata[x] = {drivername.capitalize(): qualitimes_ignored[x]['driver'],
                                  qualitimes_ignored[x]['teammatename'].capitalize(): qualitimes_ignored[x][
                                      'teammate'],
                                  "Gap": "ignored"
                                  }
                try:
                    qualidifference[x+1]['teammate']
                    columndata[x+1] = {drivername.capitalize(): qualitimestable[x+1]['driver'],
                                      qualidifference[x+1]['teammate'].capitalize(): qualitimestable[x+1]['teammate'],
                                      "Gap": qualidifference[x+1]['time']
                                      }
                except Exception:
                    columndata[x+1] = {drivername.capitalize(): qualitimes_ignored[x]['driver'],
                                     qualitimes_ignored[x+1]['teammatename'].capitalize(): qualitimes_ignored[x+1][
                                         'teammate'],
                                     "Gap": "ignored"
                                     }
            try:
                if not columndata2 or endoftheseasondata[0]['teammate'] == qualidifference[x]['teammate']:
                    try:
                        columndata[x] = {drivername.capitalize(): qualitimestable[x]['driver'],
                                         qualidifference[x]['teammate'].capitalize(): qualitimestable[x]['teammate'],
                                         "Gap": qualidifference[x]['time']
                                         }
                        columndata[x + 1] = {drivername.capitalize(): qualitimestable[x + 1]['driver'],
                                             qualidifference[x + 1]['teammate'].capitalize(): qualitimestable[x + 1][
                                                 'teammate'],
                                             "Gap": qualidifference[x + 1]['time'], "Average gap": endoftheseasondata[0]['time']
                                             }
                    except Exception as ex:
                        print(ex)
            except Exception:
                if columndata3 and endoftheseasondata[0]['teammate'] != qualitimes_ignored[x]['teammatename']:
                    columndata3[x] = {drivername.capitalize(): qualitimes_ignored[x]['driver'],
                                     qualitimes_ignored[x]['teammatename'].capitalize(): qualitimes_ignored[x][
                                         'teammate'],
                                     "Gap": "---"
                                     }
                    columndata3[x + 1] = {drivername.capitalize(): qualitimestable[x + 1]['driver'],
                                         qualidifference[x + 1]['teammate'].capitalize(): qualitimestable[x + 1][
                                             'teammate'],
                                         "Gap": qualidifference[x + 1]['time'],
                                         "Average gap": endoftheseasondata[0]['time']
                                         }
                elif columndata2 and endoftheseasondata[0]['teammate'] != qualitimes_ignored[x]['teammatename']:
                    columndata2[x] = {drivername.capitalize(): qualitimes_ignored[x]['driver'],
                                     qualitimes_ignored[x]['teammatename'].capitalize(): qualitimes_ignored[x][
                                         'teammate'],
                                     "Gap": "---"
                                     }
                    columndata2[x + 1] = {drivername.capitalize(): qualitimestable[x + 1]['driver'],
                                         qualidifference[x + 1]['teammate'].capitalize(): qualitimestable[x + 1][
                                             'teammate'],
                                         "Gap": qualidifference[x + 1]['time'],
                                         "Average gap": endoftheseasondata[0]['time']
                                         }
                else:
                    columndata[x] = {drivername.capitalize(): qualitimes_ignored[x]['driver'],
                                     qualitimes_ignored[x]['teammatename'].capitalize(): qualitimes_ignored[x]['teammate'],
                                     "Gap": "---"
                                     }
                    columndata[x + 1] = {drivername.capitalize(): qualitimestable[x + 1]['driver'],
                                         qualidifference[x + 1]['teammate'].capitalize(): qualitimestable[x + 1][
                                             'teammate'],
                                         "Gap": qualidifference[x + 1]['time'], "Average gap": endoftheseasondata[0]['time']
                                         }

            else:
                try:
                    columndata3[x] = {drivername.capitalize(): qualitimestable[x]['driver'],
                                      qualidifference[x]['teammate'].capitalize(): qualitimestable[x]['teammate'],
                                      "Gap": qualidifference[x]['time']
                                      }
                except Exception:
                    try:
                        if endoftheseasondata[0]['teammate'] == qualidifference[x]['teammate']:
                            columndata[x] = {drivername.capitalize(): qualitimestable[x]['driver'],
                                             qualidifference[x]['teammate'].capitalize(): qualitimestable[x]['teammate'],
                                             "Gap": qualidifference[x]['time']
                                             }
                    except Exception:
                        try:
                            if endoftheseasondata[0]['teammate'] == qualidifference[x+1]['teammate']:
                                pass
                            else:
                                columndata3[x] = {drivername.capitalize(): qualitimes_ignored[x]['driver'],
                                                  qualitimes_ignored[x]['teammatename'].capitalize(): qualitimes_ignored[x][
                                                      'teammate'],
                                                  "Gap": "---"
                                                  }
                        except Exception:
                            pass


                try:  # fixing for driver ban situations where the same driver comes back
                    endoftheseasondata[2]['drivers']
                    if not endoftheseasondata[0]['teammate'] == qualidifference[x]['teammate']:
                        columndata3[x + 1] = {drivername.capitalize(): qualitimestable[x + 1]['driver'],
                                              qualidifference[x + 1]['teammate'].capitalize(): qualitimestable[x + 1][
                                                  'teammate'],
                                              "Gap": qualidifference[x + 1]['time'],
                                              "Average gap": endoftheseasondata[2]['time']
                                              }
                    else:
                        break
                except Exception:
                    try:
                        if endoftheseasondata[0]['teammate'] == qualidifference[x+1]['teammate']:
                            columndata[x + 1] = {drivername.capitalize(): qualitimestable[x + 1]['driver'],
                                              qualidifference[x + 1]['teammate'].capitalize(): qualitimestable[x + 1][
                                                  'teammate'],
                                              "Gap": qualidifference[x + 1]['time'],
                                              "Average gap": endoftheseasondata[0]['time']
                                              }
                        else:
                            columndata3[x + 1] = {drivername.capitalize(): qualitimestable[x + 1]['driver'],
                                                  qualidifference[x + 1]['teammate'].capitalize(): qualitimestable[x + 1][
                                                      'teammate'],
                                                  "Gap": qualidifference[x + 1]['time'],
                                                  "Average gap": endoftheseasondata[0]['time']
                                                  }
                    except Exception:
                        try:
                            if qualitimes_ignored[x] and qualitimes_ignored[x+1]:
                                columndata[x] = {drivername.capitalize(): "no time",
                                                     qualidifference[x-1]['teammate'].capitalize(): "no time",
                                                     "Gap": "---",
                                                     "Average gap": endoftheseasondata[0]['time']
                                                     }
                        except Exception:
                            pass

    results = pd.DataFrame.from_dict(columndata, orient='index')
    print(results)

    if columndata2:
        results2 = pd.DataFrame.from_dict(columndata2, orient='index')
        print(results2)
    if columndata3:
        results3 = pd.DataFrame.from_dict(columndata3, orient='index')
        print(results3)

    # DataToGUI.gui(results, results2, results3)
    dfs = [results]
    nodata2 = False
    nodata3 = False
    results.to_csv(f'{drivername}_{season}_{endoftheseasondata[0]["teammate"]}.csv')

    try:
        if not results2.empty:
            results2.to_csv(f'{drivername}_{season}_{endoftheseasondata[1]["teammate"]}.csv')
            dfs.append(results2)
        else:
            logging.info("No data for column 'results2'")
            nodata2 = True
    except Exception:
        logging.info("No data for column 'results3'")
        nodata3 = True

    try:
        if not results3.empty:
            results3.to_csv(f'{drivername}_{season}_{endoftheseasondata[2]["teammate"]}.csv')
            dfs.append(results3)
        else:
            logging.info("No data for column 'results3'")
            nodata3 = True
    except Exception:
        logging.info("No data for column 'results3'")
        nodata3 = True

    with open(f'{drivername}_{season}_{endoftheseasondata[0]["teammate"]}.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        with open(f'{drivername}_{season}.csv', 'w', newline='') as merged:
            csv_writer = csv.writer(merged)

            for line in csv_reader:
                csv_writer.writerow(line)
            try:
                with open(f'{drivername}_{season}_{endoftheseasondata[1]["teammate"]}.csv', 'r') as csv_file2:
                    csv_reader2 = csv.reader(csv_file2)

                    with open(f'{drivername}_{season}.csv', 'r') as mergeread:
                        csv_mergereader = csv.reader(mergeread)

                        for row in csv_mergereader:
                            next(csv_reader2)

                    for row in csv_reader2:
                        csv_writer.writerow(row)
            except Exception as ex:
                print("The same teammate pair was through the whole season!")

    try:
        with open(f'{drivername}_{season}_{endoftheseasondata[2]["teammate"]}.csv', 'r') as teammate2:
            teammate2reader = csv.reader(teammate2)

            with open(f'{drivername}_{season}.csv', 'r') as mainfile:
                mainfilereader = csv.reader(mainfile)

                with open(f'{drivername}_{season}.csv', 'a', newline='') as merged2:
                    print("Races ", races)
                    teammate2writer = csv.writer(merged2)
                    index = 1

                    for line in mainfilereader:
                        print("line ", line)
                        index += 1
                        if index+10 > races:
                            for row in teammate2reader:
                                print("Line2 ", row)
                                teammate2writer.writerow(row)
    except Exception:
        print("No data for teammate 2")